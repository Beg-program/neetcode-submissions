class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const count : {[key: string]: number} ={}

        if (s.length !== t.length){
            return false
        }
        for (let i= 0; i < s.length; i++){
            if( s[i] in count ){
                count[s[i]]+=1
            }else{count[s[i]] = 1}
        }
        for (let i = 0; i< t.length; i++){
            if(t[i] in  count){
                count[t[i]] -= 1
            }else return false
        } 
        for (let i = 0; i< t.length; i++){
            if(count[t[i]] !== 0 ){
                return false
            }
        } 
        return true      

        
    }
}
