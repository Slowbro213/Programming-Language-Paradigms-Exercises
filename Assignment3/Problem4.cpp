#include <iostream>
#include <unordered_map>
#include "LinkedQueue.h"

using namespace std;


template <typename K,typename V>
class LRUCache{
private:
    unordered_map<K,Node<K,V>*> cache;
    int cap;
    LinkedListQueue<K,V> q;
public:
    LRUCache(int capacity): cap(capacity){}
    V get(K key){
        if(cache.find(key)==cache.end())
            return NULL;
        q.Enqueue(cache[key]);
        return cache[key]->value;
    }
    void put(K key,V value){
        if(cache.find(key)!=cache.end())
        {
            Node<K,V>* node =  cache[key];
            node->value=value;
            q.Enqueue(node);
            return;
        }
        else if(cache.size()==cap){
            K k = q.Dequeue();
            cache.erase(k);
        }
        q.Enqueue(key,value);
        cache[key] = q.getFirst();
    }

};

int main()
{
    LRUCache<int,int> cache(2);
    cache.put(1,1);
    cache.put(2,2);
    cout<<cache.get(1)<<endl;
    cache.put(3,3);
    cout<<cache.get(2)<<endl;
    cache.put(4,4);
    cout<<cache.get(1)<<endl;
    cout<<cache.get(3)<<endl;
    cout<<cache.get(4)<<endl;
    return 0;
}