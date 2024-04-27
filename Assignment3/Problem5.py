import io
import socket

class MicroSerializer:
    UNSERIALIZABLE_TYPES = {io.IOBase, socket.socket}
    #if youre going to use this please dont put a dictionary in your objects with a key as '___class___' , that will break it
    def __init__(self,):
            self.seen = set()

    def turn(self,dictt : dict):
        for key, value in dictt.items():
            if not isinstance(value, (int, float, str, list, tuple, set)):
                if any(isinstance(value, t) for t in MicroSerializer.UNSERIALIZABLE_TYPES):
                    self.seen.clear()
                    raise Exception("Object has Unserializable members")
                t=value
                if not isinstance(value, dict):
                    if value in self.seen:
                        self.seen.clear()
                        raise Exception("Cyclical references detected. Serialization rejected.")
                    self.seen.add(value)
                    t = value.__dict__
                    t['___class___'] = value.__class__.__name__
                dictt[key] = self.turn(t)
            elif isinstance(value,(list,tuple,set)):
                dictt[key] = self.turn2(value)
        return dictt

    def turn2(self,listt : list):
        for i in range(len(listt)):
            if isinstance(listt[i],(list,tuple,set)):
                listt[i] = self.turn2(listt[i])
            elif not isinstance(listt[i], (int, float, str, list, tuple, set)):
                d = listt[i]
                if not isinstance(listt[i],dict):
                    d = vars(listt[i])
                    d ['___class___'] = listt[i].__class__.__name__
                d = self.turn(d)
                listt[i] = d

        return listt

    def write(self, obj):
        if not isinstance(obj, (int, float, str, list, tuple, set)):
            if not isinstance(obj, dict):
                if any(isinstance(obj, t) for t in MicroSerializer.UNSERIALIZABLE_TYPES):
                    self.seen.clear()
                    raise Exception("Object is Unserializable")
                dictt = vars(obj)
                dictt['___class___'] = obj.__class__.__name__
            dictt = self.turn(dictt)
        elif isinstance(obj,(list,tuple,set)):
            dictt = self.turn2(obj)
        self.seen.clear()
        return str(dictt)

    def unturn(self,dictt):
        if isinstance(dictt,dict) and '___class___' in dictt:
            class_name = dictt['___class___']
            class_obj = globals()[class_name]

            del dictt['___class___']

            obj = class_obj.__new__(class_obj)
            class_obj.__init__(obj, *(), **{})
            for key, value in dictt.items():
                if isinstance(value, (list, tuple, set)):
                    setattr(obj, key, self.unturn2(value))
                else:
                    setattr(obj, key, self.unturn(value))
            return obj
        elif isinstance(dictt,dict):
            for key, value in dictt.items():
                if isinstance(value, (list, tuple, set)):
                    dictt[key] =  self.unturn2(value)
                else:
                    dictt[key] = self.unturn(value)
        return dictt

    def unturn2(self,obj : list):
        for i in range(len(obj)):
            if isinstance(obj[i], (list, tuple, set)):
                obj[i] = self.unturn2(obj[i])
            else:
                obj[i] = self.unturn(obj[i])
        return obj

    def read(self,obj):
        obj = eval(obj)
        if isinstance(obj, (list, tuple, set)):
            obj = self.unturn2(obj)
            return obj
        return self.unturn(obj)

class G:
    def __init__(self):
        self.a = 7
class D:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = G()

class A:
    def __init__(self):
        self.a = 1
        self.b = {
            1:2,
            2:[6,8,{11:12}],
            3:D()
        }
        self.c = [1,G(),3]
        self.d = D()

if __name__ == '__main__':
    ms = MicroSerializer()
    file = open("thanas4.txt",'w')
    #s = ms.write(file)#will throw exception as it should because you cannot serialize files
    a = A()
    d = D()
    a.d = d
    d.c = a
    #s = ms.write(a)#there will be an error here because of cyclical references as it should be
    l = [1,2,3,4,5]
    s = ms.write(l)
    print(s)
    l = ms.read(s)
    print(l[2].a , l[2].b, l[2].c , l[2].d.a , l[2].d.b , l[2].d.c.a)
