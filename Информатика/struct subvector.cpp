#include <iostream>

using namespace std;

// недовектор
struct subvector {
     int *mas;
     unsigned int top; 
     unsigned int capasity;
};

// инициализация пустого недовектора (top и capacity по нулям, а mas это NULL)
bool init(subvector* qv) {
  qv->top = 0;
  qv->capasity = 0;
  qv->mas = NULL;
  return 0;
}

// функция для удваивания массива: 
int* doubling(int* arr, unsigned int N) {
    int* arr2 = new int[2*N];
    for (unsigned int i = 0; i < N; i++){
        arr2[i] = arr[i];
    }
    delete[] arr;
    return arr2;
}

// ***** qv->capasity - размер массива, его объем, если = 0 => массив нулевой

// добавление элемента в конец недовектора с выделением дополнительной памяти при необходимости
void push_back(subvector* qv, int d) {
  // что, если размер будет = 0? new; capasity = top = 1:
  //qv->capasity <=> (*qv).capasity
  
  qv->top+=1;
  
  if (qv->capasity == 0){
    qv->mas = new int[1];
    qv->capasity = 1;    
  }
  
  // что, если top=capasity?:
  if (qv->top == qv->capasity){
    int * mas1 = doubling(qv->mas, qv->capasity);    
    qv->mas = mas1;
  }
  
  // как добавить элемент?:
  qv->mas[qv->top-1] = d;    
}

// удаление элемента с конца недовектора, значение удаленного элемента вернуть (если недовектор пустой, вернуть ноль)
int pop_back(subvector *qv){
  // если размер = 0:
  if (qv->capasity == 0) {
    return 0;
  }  
  int top1 = qv->top-1;
  return qv->mas[top1];  
}

// увеличить емкость недовектора (можно использовать и для уменьшения - тогда, в рамках данной реализации, если top меньше новой capacity, то копируем только то, что влезает, и уменьшаем top до capacity)
// сделать так, чтобы размер массива capasity стал new_capasity
bool resize(subvector *qv, unsigned int new_capacity){
  int* mas1 = new int[new_capasity];
  
  if (qv->top < new_capasity){
    for (int i = 0; i < qv->top; i++) {
      mas1[i] = qv->mas[i];
    }
  }
  
  else {
      for (int i = 0; i < qv->capasity; i++) {
        mas1[i] = qv->mas[i];
      }
      qv->top = new_capasity;
  }
  
  delete[] qv->mas;
  qv->mas = mas1;
  qv->capasity = new_capasity;
}

//void shrink_to_fit(subvector *qv); // очистить неиспользуемую память, переехав на новое место с уменьшением capacity до top
// написать ф-ю, кот оставляет в массиве столько мест для элементов сколько есть элементов. то есь если есть массив на 10, а занято только 3 места, то лишние 7 нужно удалить.
void shrink_to_fit(subvector *qv){
    // 1 - посчитать количество элементов, 2 - посчитать количество мест 3 - если мест больше, чем элементов, то удалить лишнее, если одинаково - ничего не делать.
     int* mas1 = new int[new_capasity];
     if (qv->top < capasity){
        
     
     }
    
}; 


//void clear(subvector *qv); // очистить содержимое недовектора, занимаемое место при этом не меняется

//void destructor(subvector *qv);	// очистить всю используемую память, инициализировать недовектор как пустой




int main()
{
  // тест для push_back():
   struct subvector sv;
   init(&sv);
   /* push_back(&sv, 7);
   cout << sv.mas[sv.top-1] << endl; */
  // тест для pop_back:
  
   /*push_back(&sv, 7);
   push_back(&sv, 5);
   push_back(&sv, 3);*/
   
   cout << pop_back(&sv) << endl;
   
   // тест для resize:
   
   for (int i = 0; i <= 10; i++){
      
   }
   
   /* доб
   вывести кап
   применить ф-ю
   вывести капасити 
   */
   cout << sv->capasity << endl;
   
   
   
   
   
   
    return 0;
}
