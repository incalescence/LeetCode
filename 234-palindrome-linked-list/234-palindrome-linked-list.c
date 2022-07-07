/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


bool isPalindrome(struct ListNode* head) {
    // copy the list into an array
    int array[100000];
    struct ListNode *curr = head;
    int count = 0;
    while (curr != NULL) {
        array[count] = curr->val;
        count++;
        curr = curr->next;
    }
    
    // check palindrome 
    for (int i = 0; i < count/2; i++) {
        if (array[i] != array[count-1-i]) {
            return false; 
        }
    }
    return true;

}