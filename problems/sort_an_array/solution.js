/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    const arr2 = nums.slice();
    
    for (let i = 1; i < arr2.length; i++) {
        const key = arr2[i];
        let j = i - 1;
        
        while (key < arr2[j] && j >= 0) {
            arr2[j + 1] = arr2[j];
            j--;
        }
        
        arr2[j + 1] = key;
    }
    
    return arr2;
};