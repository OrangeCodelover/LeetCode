def isValid( s: str) -> bool:
    s_1 = ""
    if len(s) <=1:
        return False
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{" :
            s_1 += s[i]
        else:
            if len(s_1) <1:
                    return False
            if  (s_1[-1] == "(" and s[i] == ")") or (s_1[-1] == "[" and s[i] == "]") or (s_1[-1] == "{" and s[i] == "}"):
                s_1 = s_1[: -1]
            else:
                return False
    if s_1 != "":
        return False
    return True    
