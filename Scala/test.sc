var a : List[Int] = List(1,2,3,4)

case class Dog(name: String, breed: String)

def lambda = {x: Int => x + 1}
val lambda2 = (x: Int)  => x + 2
lambda2(2)
lambda2.apply(3)

//a.zipWithIndex.foreach(
//  x => println(x)
//)


//object Solution {
//  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
//    var map : Map[Int, Int] = Map()
//    for(i <- nums.indices if a) {
//      var tmp = target - nums(i)
//      if(map.contains(tmp)){
//        Array(map(tmp), i)
//      }
//      map += (nums(i) -> i)
//    }
//    null
//  }
//}
//
//Solution.twoSum(Array(1,2,3,4), 5)