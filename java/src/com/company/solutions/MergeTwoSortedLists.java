package com.company.solutions;

public class MergeTwoSortedLists {

    private class ListNode{
        int val;
        ListNode next;
        ListNode(){}
        ListNode(int val){this.val = val;}
        ListNode(int val, ListNode next){this.val = val; this.next = next;}
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        ListNode root = new ListNode();
        ListNode pointer = root;


        while (l1 != null && l2 != null){
            if (l1.val < l2.val){
                pointer.next = l1;
                l1 = l1.next;

            }else{
                pointer.next = l2;
                l2 = l2.next;
            }

            pointer = pointer.next;
        }

        if (l1 != null){
            pointer.next = l1;
        }
        if (l2 != null){
            pointer.next = l2;
        }


        return root.next;
    }
}
