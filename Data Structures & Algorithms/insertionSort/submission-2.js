/**
 * Pair class to store key-value pairs
 */
// class Pair {
//     /**
//      * @param {number} key The key to be stored in the pair
//      * @param {string} value The value to be stored in the pair
//      */
//     constructor(key, value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[][]}
     */
    insertionSort(pairs) {
        /*
            start at index 1
            iterate from 1 to length
                iterate from index to 0
                    check if index below is less than current index
                        swap if yes
                
        */

        const result = [];
        if (pairs.length === 0) return result
        result.push([...pairs]);
        for (let i = 1; i < pairs.length; i++) {
            for (let j = i; j > 0; j--) {
                if (pairs[j].key < pairs[j - 1].key) {
                    const temp = pairs[j - 1];
                    pairs[j - 1] = pairs[j];
                    pairs[j] = temp;
                }
            }
            result.push([...pairs]);
        }
        return result;
    }
}

// class Solution {
//     /**
//      * Entry point for the Insertion Sort algorithm
//      * @param {Pair[]} pairs Array of Pair objects to be sorted
//      * @returns {Pair[][]} Array containing the state of the array at each step
//      */
//     insertionSort(pairs) {
//         const n = pairs.length;
//         const res = []; // To store the intermediate states of the array

//         for (let i = 0; i < n; i++) {
//             let j = i - 1;

//             // Move elements that are greater than key one position ahead
//             while (j >= 0 && pairs[j].key > pairs[j + 1].key) {
//                 [pairs[j], pairs[j + 1]] = [pairs[j + 1], pairs[j]];
//                 j -= 1;
//             }

//             // Clone and save the entire state of the array at this point
//             res.push([...pairs]);
//         }

//         return res;
//     }
// }
