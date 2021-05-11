const start = 235741
const end = 706948
const part = 2
let current = start

// 1. It is a six-digit number.
// 2. The value is within the range given in your puzzle input.
// 3. Two adjacent digits are the same (like 22 in 122345).
// 4. Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

// check if arr[i] is equal to arr[i+1]
// beware of array out of bound, make sure i+1 is valid
let checkAdjacent = (arr, i) => {
    if (arr[i] === arr[i + 1]) {
        return true
    } else {
        return false
    }
}

// check if arr[i] is equal or less than arr[i+1]
// beware of array out of bound, make sure i+1 is valid
let checkIncrement = (arr, i) => {
    if (arr[i] <= arr[i + 1]) {
        return true
    } else {
        return false
    }
}

let increaseValue = (value, i) => {
    // skip some iteration by increasing from failing value 
    // 235741, next iteration should check for 235751
    // i = 3 will fail, we can increase value of current[4], which means increase by 10 = 10 * 1
    // 6 - 2 - 3 = 1
    // 231242, next iteration should check for 232242
    // i = 1 will fail, need to increase value of current[2], means increase by 1000 = 10 ** 3
    // 6 - 2 - 1 = 3 
    // 233332, next iteration should check for 233333
    // i = 4 will fail, need to increase value of current[5], means increase by 1 = 10 ** 0
    // 6 - 2 - 4 = 0
    // general equation: (current.length - 2 - i )** 10

    let len = value.toString().length
    let newValue = value + (10 ** (len - i - 2))

    return newValue
}

let iter = 0
let valid = 0

while (current <= end) {
    iter++

    let adjacentCount = 0
    let isAlwaysIncrement = true

    // convert current number to array
    let currentArray = current.toString().split('')
    
    // loop until length - 1 since all function already checks up to i + 1
    for (let i = 0; i < currentArray.length - 1; i++) {
        // check for rules 3, if exists add adjacentCount
        if (checkAdjacent(currentArray, i)) {
            if (part === 1 || currentArray.filter(e => e == currentArray[i]).length === 2) {
                adjacentCount++
            }
        }

        // check rules 4, if false stop for loop and increase value
        if (!checkIncrement(currentArray, i)) {
            isAlwaysIncrement = false
            current = increaseValue(current, i)
            break;
        }

        // always increase value if loop ends normally
        if (i === currentArray.length - 2) {
            current = increaseValue(current, i)
        }
    }

    if (isAlwaysIncrement && adjacentCount >= 1) {
        // if all rules are satisfied, count as valid password
        valid++
    }
}

console.log(valid, iter)