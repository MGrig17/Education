// struct listing
#include <iostream>

using namespace std;

struct subforwardlist {

    int data;

    subforwardlist* next;

};

//инициализация пустого недосписка: // двойной указатель--------------------------------------------------------------------------------------------------------------
bool init(subforwardlist **sfl){
    *sfl = NULL;
    return 0;
}; 	

// NULL <=>end

//добавление элемента в конец недосписка:-----------------------------------------------------------------------------------------------------------------------------------
bool push_back(subforwardlist **sfl, int d){
    //  если пустой список:
    if (*sfl == NULL) {
        subforwardlist* new_list = new subforwardlist;  // создали
        new_list->data = d; // добавили дату
        new_list->next = NULL; // обозначили последним
        *sfl = new_list; // переобозначили последним
    }
    // не пустой:
    else {
        subforwardlist* new_list = new subforwardlist;  // создали
        new_list->data = d; // добавили дату
        new_list->next = NULL; // обозначили последним
        
        // тмп
        subforwardlist* tmp; // создаем тмп
        tmp = *sfl; // это  по сути счетчик-указатель! или временная переменная        
        while(tmp->next != NULL) {
            tmp = tmp->next;            
        }
        tmp->next = new_list;
    }
    return 0;
};

//удаление элемента с конца недосписка, если пустой - возвращать 0------------------------------------------------------------------------------------------------------------
int pop_back_fignya(subforwardlist **sfl){
    // если пустой:
    if (*sfl == NULL) {
        return 0;
    }
    // если 1 элемент
    subforwardlist* tmp; // создаем тмп
    tmp = *sfl;
    if (tmp->next == NULL){
        int n1 = tmp->data;
        delete tmp;
        tmp = NULL;
        return n1;
    }
    // не пустой:
    else {        
        //идея идти до предпоследнего элемента, указателем предпоследнего указывать на NULL, delete последний
        while(tmp->next->next != NULL) {
            tmp = tmp->next;            
        }
        
        //tmp->next = NULL;
        int n = tmp->next->data; // сохр значение
        delete tmp->next;
        tmp->next = NULL;
        return n;
    }
};

int pop_back(subforwardlist **sfl) {
  if (*sfl == NULL) {
    return 0;
  }
  else {
    subforwardlist* tmp;
    tmp = *sfl;
    if (tmp->next == NULL) {
      *sfl = NULL;
      int a = tmp->data;
      delete tmp;
      return a;
    }
    else {
      while (tmp->next->next != NULL) {
        tmp = tmp->next;
      }
      int a = tmp->next->data;
      delete tmp->next;
      tmp -> next = NULL;
      return a;
    }
  }
}

//добавление элемента в начало недосписка--------------------------------------------------------------------------------------------------------------------------
bool push_forward(subforwardlist **sfl, int d){
    subforwardlist* new_list = new subforwardlist;  // создали
    new_list->data = d; // добавили дату
    //subforwardlist* old_list_const = *sfl;
    
    new_list->next = *sfl;
    *sfl = new_list;
    //new_list->next = old_list_const;
    //delete old_list_const;
    return 0;
}; 

//удаление элемента из начала недосписка, если пустой - возвращать 0-----------------------------------------------------------------------------------------------
int pop_forward(subforwardlist **sfl){
    subforwardlist* tmp; // создаем тмп
    tmp = *sfl;
    // если пустой:
    if (*sfl == NULL) {
        return 0;
    }
    
    // не пустой:
    else {
        *sfl = tmp->next;
        int n = tmp->data;
        delete tmp;
        return n;        
    }    
};

//добавление элемента с порядковым номером where ********************************************************************
bool push_where1(subforwardlist **sfl, unsigned int where, int d){
    if (sfl == NULL) {
    return 0;
  } 
    subforwardlist* new_list = new subforwardlist;  // создали вставляемый элемент
    new_list->data = d; // добавили дату
    subforwardlist* tmp; // создаем тмп
    tmp = *sfl; // это  по сути счетчик-указатель! или временная переменная
    
    
    if (where == 0){
        push_forward(sfl, d);
    }
    else {
    	
    	if (tmp == NULL){
    		return 0;
    	}
    	else {
    		unsigned int m = 1;
    	
        	while (m != where) {
        	m+=1;
        	tmp = tmp->next;
        	}
        	new_list->next=tmp->next;
        	tmp->next=new_list;              
        
        }
           /* if (tmp != 0){
            
                if (tmp->next != NULL){
                    tmp = tmp->next;   
                }
                else {
            
                }
            new_list->next=tmp->next; // 
            tmp->next=new_list;
            }*/
        
           
        }
    return 0;
};


bool push_where(subforwardlist **sfl, unsigned int where, int d) {
        subforwardlist* new_list= new subforwardlist;
        new_list->data=d;
        subforwardlist*tmp;
        tmp =*sfl;


        if (tmp==NULL) {return 0; }
        else {
        for (unsigned int i=0;i!=where;i++) {
            tmp=tmp->next;
        }
        new_list->next=tmp->next;
        tmp->next=new_list;

        }

return 0 ;
}


//**********************************************************************************************************************
//удаление элемента с порядковым номером where----------------------------------------------------------------------------------------------------------------------
/*int erase_where(subforwardlist **sfl, unsigned int where){
    subforwardlist* tmp; // создаем тмп
    tmp = *sfl; // это  по сути счетчик-указатель! или временная переменная
    unsigned int m = 0; // счетчик where
    while (m != where ) {
        m+=1;        
        tmp = tmp->next;        
    }
    int n = tmp->next->data;
    delete tmp->next;
    tmp->next = tmp->next->next;
    return n;    
};	*/

//удаление элемента с порядковым номером where
int erase_where(subforwardlist **sfl, unsigned int where) {
        if (*sfl == NULL) {
        return 0;
    }
        
        subforwardlist *tmp = *sfl;
        for (unsigned int i = 1;  i < where-1; i++){
            tmp = tmp -> next;
        }
        subforwardlist *to_delete = tmp->next;
        tmp -> next = to_delete -> next;
        delete to_delete;
        return 0;
    }

//очистить содержимое недосписка, если пустой - возвращать 0----------------------------------------------------------------------------
void clear1(subforwardlist  **sfl){
    
    subforwardlist* tmp; // создаем тмп
    subforwardlist* tmp1;
    tmp = *sfl;
    // если пустой:
    if (*sfl == NULL) {
        //cout << 0 << endl;
    }
    // не пустой:
    else {
        if (tmp->next == NULL){
            delete tmp;
        }
        else {
        while(tmp->next != NULL) {
            tmp1 = tmp->next;
            delete tmp;
            tmp = tmp1;
        }    
        }
        delete tmp;
        *sfl = NULL;
        //cout << 1 << endl;
    }
    
};



//определить размер недосписка-----------------------------------------------------------------------------------------------------------
unsigned int size(subforwardlist  *sfl){
    if (sfl == NULL) {
        return 0;
    }
    
    subforwardlist* tmp;
    tmp = sfl;
    unsigned int size = 0;
    while (tmp != NULL) {
        size++;
        tmp = tmp->next;
    }
    //for(subforwardlist* sfl;   )
    
    return size;
};

void clear(subforwardlist **sfl) {
//cout << "!!!!!!!"<< endl;
    while (*sfl != NULL) {
        pop_forward(sfl);
        
    }
}

// comment - void init(subforwardlist** sfl) {}

// ваш код сюда идет
  

int main (){
    //инициализация
   subforwardlist* sfl;
   init(&sfl);
   
   push_back(&sfl, 100);
   push_back(&sfl, 100);
   //push_back(&sfl, 100);
   
   cout << "size = "<< size(sfl) << endl;
   
   cout << "push_where " << push_where1(&sfl, 2, 666) << endl;
   
   cout << "size = "<< size(sfl) << endl;
   
   cout << "elements: "<< endl;
   
   cout << "size = "<< size(sfl) << endl;
   /*
   do {
      cout << sfl -> data << endl;
      sfl = sfl->next;
   } while (sfl != NULL);
   */
   cout << "size = "<< size(sfl) << endl;
   
   clear(&sfl); 
   
   
    return 0;
}
