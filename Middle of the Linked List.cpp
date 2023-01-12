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
    ListNode* middleNode(ListNode* head) {
        int middle;
        int count=1;
        int chake=1;
        ListNode* temp=head->next;

        while( temp!=NULL){
            temp = temp->next;
            count++;
           // cout<<"done";
            cout<< count<<","<<endl;
           cout <<endl;
        }
        // if (count%2!=0){
        //     count++;
        // }
        middle=ceil(count/2)+1;
        cout<<middle;
        temp=head;
        while(temp!= NULL && middle!=chake){
            temp=temp->next;
            chake++;
           // cout<<"done2";


        }
        return temp;
    }

};
