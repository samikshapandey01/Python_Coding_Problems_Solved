def norm(v,p=2): # function norm with default value of p as 2 which returns Euclidean norm of v
  
  sqr_sum_v=0 # variable to store pth power sum of values in v
  for x in v:
        sqr_sum_v=sqr_sum_v+x**p 
  v_norm_value=sqr_sum_v**(1/p) #final variable to calculate p norm value of v
  return v_norm_value

v_norm=norm([4,3,3],3) # calling the function with p=3 and passing list of 3 values
print(f"norm([4,3,3],3) : {v_norm}")

v_norm_euc=norm([6,8]) # calling the function to return euclidean norm of v norm(v) i.e p=2
print(f"norm([6,8]) : {v_norm_euc}")