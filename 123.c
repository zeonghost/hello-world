#include <stdio.h>
#include <conio.h>
#include <stdbool.h>
#include <string.h>

#define S 50

typedef struct node *nd;
struct node
{
       int n;
       nd next;
}NODE;

void getExpression(char []);
void createStack(nd *);
void push(nd *, int);
int pop(nd *);
bool isEmpty(nd);
void displayResult(char [], int);
bool processExpression(char []);

int main(void)
{
    bool ok;
    char post[S];
    getExpression(post);
    ok = processExpression(post);
    
    if(!ok)
    {
           printf("\n\n%s was not processed properly. It was an invalid expression! ",post);
           getch();
    }
    return 0;
}

void getExpression(char post[])
{
     printf("\n\nInput a postfix expression: ");
     gets(post);
     return;
 }
 
void createStack(nd *top)
{
     *top = NULL;
}

void push(nd *top, int num)
{
     nd temp;
     
     temp = malloc(sizeof(NODE));
     temp -> n = num;
     temp -> next = NULL;
     
     temp -> next = *top;
     *top = temp;
}

int pop(nd *top)
{
    int rNum;
    nd tp;
    
    tp = *top;
    rNum = tp -> n;
    *top = tp -> next;
    free(tp);
    
    return rNum;
}

bool isEmpty(nd top)
{
     bool empty = false;
     if (top == NULL)
        empty = true;
     return empty;
}

void displayResult(char post[], int res)

{
     printf("\n\n%s = %d",post,res);
     getch();
     return;
}

bool processExpression(char post[])
{
     char ch;
     int i = 0, num, num1, num2, result;
     bool empty;
     nd top;
     
     createStack(&top);
     
     while (post[i] != '\0')
     {
           ch = post[i];
           if ((ch == '+') || (ch == '*') || (ch == '/') || (ch == '-'))
           {
                   empty = isEmpty(top);
                   if (!empty)
                         num1 = pop(&top);
                   else
                   {
                       printf("\n\nError: Stack is empty");
                       getch();
                       return false;
                   }
                   empty = isEmpty(top);
                   if (!empty)
                         num2 = pop(&top);
                   else
                   {
                       printf("\n\nError: Stack is empty");
                       getch();
                       return false;
                   }
                   switch(ch)
                   {
                          case '+': result = num1 + num2;
                                    break;
                          case '-': result = num2 - num1;
                                    break;
                          case '*': result = num1 * num2;
                                    break;
                          case '/': result = num2 / num1;
                                    break;   
                        
                   }
                   push(&top, result);
           }// end of if ((ch == '+') || (ch == '*') || (ch == '/') || (ch == '-'))
           else if(isdigit(ch))
           {
               num = ch - '0';
               push(&top, num);
               
           }
             else 
		   {
		   
		   return false; 
		   break;
		   }
		    

		   // end of else''
           i++;
     }// end of while (post[i] != '\0')
     empty = isEmpty(top);
     if (!empty)
          num1 = pop(&top);
     else
     {
         printf("\n\nError: Stack is empty");
         getch();
         return false;
     }
      if (top != NULL)
      {
      	return false;
      }
     displayResult(post, num1);
     return true;
}

