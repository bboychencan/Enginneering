package com.chen.service;

import com.chen.dao.UserDao;
import com.chen.dao.UserDaoImpl;

/**
 * @Author: evanchen
 * @Email: chencan@didiglobal.com
 * @Date: 2021/5/26 2:19 PM
 * @Description:
 */
public class UserServiceImpl implements UserService {

  private UserDao userDao = new UserDaoImpl();

  @Override
  public void getUser() {
    userDao.getUser();
  }
}
