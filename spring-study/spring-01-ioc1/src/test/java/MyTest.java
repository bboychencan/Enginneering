import com.chen.service.UserService;
import com.chen.service.UserServiceImpl;

/**
 * @Author: evanchen
 * @Email: chencan@didiglobal.com
 * @Date: 2021/5/26 2:20 PM
 * @Description:
 */
public class MyTest {

  public static void main(String[] args) {
    UserService userService = new UserServiceImpl();
    userService.getUser();
  }
}
