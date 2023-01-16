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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* mynode=head;
        ListNode* nxtnode=head;
        if (head==NULL){
            return head;
        } 
        else
        {while (mynode->next!=NULL ){
           // nxtnode=mynode->next;
            nxtnode=mynode->next;
            if (mynode->val==nxtnode->val){
                mynode->next=nxtnode->next;
               // delete nxtnode;
                cout<<"h";
            }
             if (mynode->val!=nxtnode->val){
                 mynode=mynode->next;
                 cout<<"i";
             }
        }
}
        
   return head; }
};
