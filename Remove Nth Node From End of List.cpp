
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
       int counter=0;
        int delet=0;
        int trace=0;
        ListNode* count=head;
        ListNode* current=head->next;
        ListNode* previous=head;

        while(count !=NULL) {
            count=count->next;
            counter++;
        }

        delet=(counter-n);
        //cout<<delet;
        int counter1=1;
        //cout<<counter;
        // if(counter==1){
        //     delete previous ;
        // }
        cout << delet;
        if(previous->next == nullptr){
            //delete previous;
            head = nullptr;
        } else if(delet == 0){
            head = head->next;
        }
        while(counter1 < delet) {
            //if(current !=NULL) {
            
            previous = previous->next;
            current = current->next;
            counter1++ ;
        }
        //cout<<"c="<<counter;

        // if(counter==3) {
        //     delete previous;
        //     head=NULL;
        // }

        if( delet + 1 == counter){
            //if(current->next=NULL)
            previous->next = nullptr;
            //delete current;
        } else if(current->next != nullptr){
           previous->next=current->next;
            //delete current;}
        }
        
        return head;
    } 
    
};// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode() : val(0), next(nullptr) {}
//  *     ListNode(int x) : val(x), next(nullptr) {}
//  *     ListNode(int x, ListNode *next) : val(x), next(next) {}
//  * };
//  */
// class Solution {
// public:
//     ListNode* removeNthFromEnd(ListNode* head, int n) {
//         int counter=0;
//         int delet;
//         ListNode* count=head;
//         ListNode*current=head->next;
//         ListNode*privious=head;

//         while(count!=NULL){
//             count=count->next;
//             counter++;
//         }
//         delet=(counter-n)+1;
//         if(counter)
//         while(current )

    
        
        
//     return head;
//     }
// };
