class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
    
        dirs = [p for p in path.split("/") if p != ""]
        
        for d in dirs:
            if d == "..":
                if res: res.pop()
                continue
            elif d == ".":
                continue
            else:
                res.append(d)

        return "/" + "/".join(res)