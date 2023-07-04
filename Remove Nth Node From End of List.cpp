
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
        int counter1=1;
        cout << delet;
        if(previous->next == nullptr){
            head = nullptr;
        } else if(delet == 0){
            head = head->next;
        }
        while(counter1 < delet) {
            previous = previous->next;
            current = current->next;
            counter1++ ;
        }
        
        if( delet + 1 == counter){
           
            previous->next = nullptr;
            
        } else if(current->next != nullptr){
           previous->next=current->next;
           
        }
        
        return head;
    } 
    
};
