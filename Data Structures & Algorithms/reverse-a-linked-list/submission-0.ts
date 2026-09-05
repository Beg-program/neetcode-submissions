/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */


class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head: ListNode | null): ListNode {
        if(head === null) return null
        else{
        let prev = null
        let curr = head 
        let nex = curr.next
        while(curr){
            curr.next = prev
            prev = curr
            curr = nex
            if(nex){nex = nex.next}
        } 
        return prev
        }
        

    }
}
