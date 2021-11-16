/**
 * @Author: evanchen
 * @Email: chencan@didiglobal.com
 * @Date: 2021/10/28 8:16 PM
 * @Description:
 */
class c {
  def test(args: Array[String]): Unit = {
    val ll = List(1,2,3,4)
    ll.foreach(println)
  }
}

object HH{

  def main(args: Array[String]): Unit = {
    val array = Array(87, 44, 5, 4, 200, 10, 39, 100)
    val set = Set(1, 2, 3, 4)
    array.filter(_ < 100).foreach(println)
    println(set.mkString(">", ",", "<"))
  }
}
