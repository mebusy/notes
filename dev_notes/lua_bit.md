...menustart

- [bit operation implemented in lua](#ab88a2280abcea190021fd76e4a5b8ef)

...menuend


<h2 id="ab88a2280abcea190021fd76e4a5b8ef"></h2>


# bit operation implemented in lua

```lua

module ("bit", package.seeall)

function lshift( num , nbit )
    num = math.floor(num)
    nbit = math.floor(nbit)
    --不考虑越界
    return num * math.pow( 2, nbit )
end

function rshift( num , nbit )
    num = math.floor(num)
    nbit = math.floor(nbit)
    --不考虑越界
    local n = math.floor( num / math.pow( 2, nbit ))
    if num < 0 then
        n = math.floor( 0x80000000 /math.pow( 2, nbit-1 ) + n)
    end
    return n
end

function bnot( num , nbit )
    return -num -1
end

local t_and =
{
    { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 },
    { 0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
    { 0,0,2,2,0,0,2,2,0,0,2,2,0,0,2,2 },
    { 0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3 },
    { 0,0,0,0,4,4,4,4,0,0,0,0,4,4,4,4 },
    { 0,1,0,1,4,5,4,5,0,1,0,1,4,5,4,5 },
    { 0,0,2,2,4,4,6,6,0,0,2,2,4,4,6,6 },
    { 0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7 },
    { 0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8 },
    { 0,1,0,1,0,1,0,1,8,9,8,9,8,9,8,9 },
    { 0,0,2,2,0,0,2,2,8,8,10,10,8,8,10,10 },
    { 0,1,2,3,0,1,2,3,8,9,10,11,8,9,10,11 },
    { 0,0,0,0,4,4,4,4,8,8,8,8,12,12,12,12 },
    { 0,1,0,1,4,5,4,5,8,9,8,9,12,13,12,13 },
    { 0,0,2,2,4,4,6,6,8,8,10,10,12,12,14,14 },
    { 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 },
}

local t_or =
{
    { 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 },
    { 1,1,3,3,5,5,7,7,9,9,11,11,13,13,15,15 },
    { 2,3,2,3,6,7,6,7,10,11,10,11,14,15,14,15 },
    { 3,3,3,3,7,7,7,7,11,11,11,11,15,15,15,15 },
    { 4,5,6,7,4,5,6,7,12,13,14,15,12,13,14,15 },
    { 5,5,7,7,5,5,7,7,13,13,15,15,13,13,15,15 },
    { 6,7,6,7,6,7,6,7,14,15,14,15,14,15,14,15 },
    { 7,7,7,7,7,7,7,7,15,15,15,15,15,15,15,15 },
    { 8,9,10,11,12,13,14,15,8,9,10,11,12,13,14,15 },
    { 9,9,11,11,13,13,15,15,9,9,11,11,13,13,15,15 },
    { 10,11,10,11,14,15,14,15,10,11,10,11,14,15,14,15 },
    { 11,11,11,11,15,15,15,15,11,11,11,11,15,15,15,15 },
    { 12,13,14,15,12,13,14,15,12,13,14,15,12,13,14,15 },
    { 13,13,15,15,13,13,15,15,13,13,15,15,13,13,15,15 },
    { 14,15,14,15,14,15,14,15,14,15,14,15,14,15,14,15 },
    { 15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15 },
}


function band( num1 , num2 )
    local bDoubleNegative = false
    if num1 <0 and num2 <0 then
        bDoubleNegative = true
    end
    
    
    num1 = string.format("%X" , num1 )
    num2 = string.format("%X" , num2 )
    
    local t1 = {}
    string.gsub( num1 , '[0-9A-F]' , function(w) table.insert(t1, 1, tonumber(w,16) ) end )
    local t2 = {}
    string.gsub( num2 , '[0-9A-F]' , function(w) table.insert(t2, 1, tonumber(w,16) ) end )
    
    --print( "aaaa" , num1, num2 )
    --[[
    	for i=1,#t1 do
     print ( i, t1[i])
    	end
    	for i=1,#t2 do
     print ( i, t2 [i])
    	end
    	--]]
    local sum = ""
    local n = math.max( #t1, #t2 )
    for i=1,n do
        local val1 = t1[i] or 0
        local val2 = t2[i] or 0
        local result = t_and[ val1+1 ] [ val2+1 ] or 0
        --print ( val1 , val2 , result  )
        sum = string.format( "%X%s" , result , sum  )
    end
    
    if bDoubleNegative then
        sum = string.gsub( sum , "^F+" , "")
        return  -(math.pow( 16, string.len(sum) )-(tonumber(sum, 16) or 0) )
        else
        return tonumber(sum, 16)
    end
end


function bor( num1 , num2 )
    local bDoubleNegative = false
    if num1 <0 or num2 <0 then
        bDoubleNegative = true
    end
    
    
    num1 = string.format("%X" , num1 )
    num2 = string.format("%X" , num2 )
    
    local t1 = {}
    string.gsub( num1 , '[0-9A-F]' , function(w) table.insert(t1, 1, tonumber(w,16) ) end )
    local t2 = {}
    string.gsub( num2 , '[0-9A-F]' , function(w) table.insert(t2, 1, tonumber(w,16) ) end )
    
    --print( "aaaa" , num1, num2 )
    --[[
    	for i=1,#t1 do
     print ( i, t1[i])
    	end
    	for i=1,#t2 do
     print ( i, t2 [i])
    	end
    	--]]
    local sum = ""
    local n = math.max( #t1, #t2 )
    for i=1,n do
        local val1 = t1[i] or 0
        local val2 = t2[i] or 0
        local result = t_or[ val1+1 ] [ val2+1 ] or 0
        --print ( val1 , val2 , result  )
        sum = string.format( "%X%s" , result , sum  )
    end
    
    --print("bbbb" , sum)
    
    if bDoubleNegative then
        sum = string.gsub( sum , "^F+" , "")
        return  -(math.pow( 16, string.len(sum) )-(tonumber(sum, 16) or 0))
        else
        return tonumber(sum, 16)
    end
end
```
