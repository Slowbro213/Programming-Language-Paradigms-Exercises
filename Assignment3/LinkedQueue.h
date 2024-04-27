#include <iostream>
#ifndef LINKED_QUEUE_H
#define LINKED_QUEUE_H
using namespace std;

//here i have made a doubly linked list and a queue using that linked list

template <typename T,typename E>
class LinkedListQueue;
template <typename K,typename V>
class LRUCache;

template <typename T,typename E>
class Node {
private:
    T key;
    E value;
    Node<T,E>* next;
    Node<T,E>* prev;
    Node(T x,E v) : key(x), value(v) , next(nullptr), prev(nullptr) {}
    Node(T x,E v, Node<T,E>* next) :  key(x), value(v), next(next), prev(nullptr) {}
    Node(T x,E v, Node<T,E>* next, Node<T,E>* prev) : key(x), value(v), next(next), prev(prev) {}
public:
    Node() : next(nullptr), prev(nullptr) {}
    friend class LinkedListQueue<T,E>;
    friend class LRUCache<T,E>;
};

template <typename T,typename E>
class LinkedListQueue{
private:
    Node<T,E>* header;
    Node<T,E>* trailer;
    int Size;

    void AddBetween(T x, E v, Node<T,E>* one, Node<T,E>* two) {
        one->next = new Node<T,E>(x,v, two, one);
        two->prev = one->next;
    }

public:
    LinkedListQueue() : Size(0) {
        header = new Node<T,E>();
        trailer = new Node<T,E>();
        header->next = trailer;
        trailer->prev = header;
    }

    LinkedListQueue(T x,E v) : LinkedListQueue() {
        AddBetween(x,v, header, trailer);
        Size = 1;
    }

    void Enqueue(T x,E v){
        AddBetween(x,v, header, header->next);
        Size++;
    }

    void Enqueue(Node<T,E>* x)
    {
        MoveBetween(x,header,header->next);
    }

    T Dequeue(){
         if (isEmpty()) {
            throw runtime_error("Queue is empty");
        }

        Node<T, E>* removed = trailer->prev;
        if (removed == nullptr || removed->prev == nullptr) {
            throw runtime_error("Unexpected null pointer encountered");
        }

        trailer->prev = removed->prev;
        trailer->prev->next = trailer;
        T data = removed->key;
        delete removed;
        Size--;
        return data;
    }

    bool isEmpty(){
        return Size == 0;
    }


    void MoveBetween(Node<T,E>* x ,Node<T,E>* one, Node<T,E>* two)
    {
        if(x->prev != nullptr && x->next!=nullptr){
        Node<T,E>* temp = x->prev;
        x->next->prev=temp;
        x->prev->next=x->next;
        }
        one->next = x;
        two->prev = one->next;
        x->prev=one;
        x->next=two;
    }

    T getHead(){
        return header->next->data;
    }

    T getTail(){
        return trailer->prev->data;
    }

    Node<T,E>* getFirst()
    {
        return header->next;
    }

    Node<T,E>* getLast()
    {
        return trailer->prev;
    }


    ~LinkedListQueue() {
        while (!isEmpty()) {
            Dequeue();
        }
        delete header;
        delete trailer;
    }
};

#endif