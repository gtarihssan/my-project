"""import pytest

from django.contrib.auth.models import User


def test_check():
    print('success test')
    assert 1==1

def test_check_for_rapport():
    print('fail test')
    assert 1!=2

def test_user(db):
    print('user created successfully')
    user=User.objects.create_user('hssan' , 'hssan@gmail.com' , 'hssan')
    num=User.objects.count()
    assert num==1

def test_user_delete(db):
    print('delete user ')
    user=User.objects.create_user('hssan', 'hssan@gmail.com' ,  'hssan')
    user.delete()
    num=User.objects.count()
    assert num == 0

"""