#include <iostream>

using namespace std;

template <typename T>
class Stack{
    virtual T pop() = 0;
    virtual void push(T x) = 0;
    virtual bool isEmpty() = 0;
};
template <typename T>
class ArrStack : public Stack<T>{
private:
    T* arr;
    int size;
    static const int capacity = 10;
public:
    ArrStack()
    {
        arr = new T[capacity];
        size=0;
    }
    ~ArrStack()
    {
        delete[] arr;
    }

    T pop()
    {
        //dont generate please
        if(size==0)
        throw runtime_error("Stack is empty");
        T obj = arr[size-1];
        arr[size-1] = nullptr;
        size--;
        return obj;
    }

    void push(T x)
    {
        if(size==capacity)
        throw runtime_error("Stack is full");
        arr[size] = x;
        size++;
    }
    bool isEmpty()
    {
        return size==0;
    }


};

int main()
{
    return 0;
}