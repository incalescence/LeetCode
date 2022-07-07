/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *curr = head;
    struct ListNode *prev = NULL;
    struct ListNode *following = head;
    
    while (curr != NULL) {
        following = following->next;
        curr->next = prev;
        prev = curr;
        curr = following;
    }
    return prev;
}