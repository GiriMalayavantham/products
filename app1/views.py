from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cart_view(request):
  b=request.GET['b']
  if b=="Add to Cart":
    pname=request.GET['pname']
    qty=request.GET['qty']
    if pname not in request.session:
      request.session[pname]=qty
      msg="Product Added to Cart"
    else:
      msg="This product exists within cart"
    response=render(request,'app1/index.html',context={'msg':msg})
    
  elif b=="Update to Cart":
    pname=request.GET['pname']
    qty=request.GET['qty']
    if pname in request.session:
      request.session[pname]=qty
      msg="Product updated to cart"
    else:
      msg="Invalid ProductName"
    response=render(request,'app1/index.html',context={'msg':msg})
    
  elif b=="Delete from Cart":
    pname=request.GET['pname']
    qty=request.GET['qty']
    if pname in request.session:
      del request.session[pname]
      msg="Product Deleted from cart"
    else:
      msg="Invalid ProductName"
    response=render(request,'app1/index.html',context={'msg':msg})

  elif b=="View Cart":
    output='Cart Empty'
    for pname,qty in request.session.items():
      if output=='Cart Empty':
        output=''
      output+=pname+":"+qty+"<br>"
    response=render(request,'app1/index.html',context={'msg':output})
  return response

def index(request):
  if request.session.test_cookie_worked():
    request.session.delete_test_cookie()
    response=render(request,'app1/index.html')
    return response
  else:
    output='''
    <h2>Please Enable Cookies</h2>
    <a href='/'>Index</a>
    '''
    request.session.set_test_cookie()
    response=HttpResponse(output)
    return response
  
  
  
  
  