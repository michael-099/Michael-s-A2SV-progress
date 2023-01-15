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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *x = new ListNode(0);
        ListNode *current = x;

        while(list1 && list2) {
            if(list1 -> val <= list2 -> val) {
                current -> next = list1;
                list1 = list1 -> next;
            }else {
                current -> next = list2;
                list2 = list2 -> next;
            }
            current = current -> next;
        }

        while(list1) {
            current -> next = list1;
            list1 = list1 -> next;
            current = current -> next;
        }

        while(list2) {
            current -> next = list2;
            list2 = list2 -> next;
            current = current -> next;
        }

        return x -> next;

    }
        
};
