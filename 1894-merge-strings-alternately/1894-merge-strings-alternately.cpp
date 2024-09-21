class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string returnString{""};
        int n{static_cast<int>(std::max(word1.length(), word2.length()))};
        for (int i{0}; i < n; i++) {
            if (word1 != "") {
                returnString += word1.front();
                word1 = word1.substr(1);
            }
            if (word2 != "") {
                returnString += word2.front();
                word2 = word2.substr(1);
            }
        }
        return returnString;
        
    }
};