

import scala.io.Source

object hw {
  
  final val STOP_WORDS = Set("ON",  "FOR", "IS", "THE",  "I", "A", "IN", "ME", "BE", "OF","AND", "MY", "YOUR",  "ON", "YOU",
      "IT", "TO", "HERE", "THERE", "GO")
  final val FREQUENCE_THRESHOLD = 30
  
  final val NUM_DISPLAY = 7
  final val FILE_PATH = "top40.sql"
  final val PATTERN = "'([^']+)'[^']+'([^']+)',\\s+(\\d)".r
      
  def countList(list: List[String]) = {
    list.foldLeft(Map.empty[String, Int]) { (dict, word) => dict + (word -> (dict.getOrElse(word, 0) + 1)) }
  }


  def main(args: Array[String]): Unit = {

    val data = Source.fromFile(FILE_PATH).getLines().toList

    val recoreds = data.map {
      case line =>
        
        val matched = PATTERN.findAllIn(line).matchData.map {
          case m =>
            val artistName = m.group(1)
            val rawTitle = m.group(2)
            val numone = m.group(3).trim == "1"

            val title = rawTitle.replaceAll("[^a-zA-Z]", " ").split("\\s+").map(_.toUpperCase)
            (artistName, title, numone)
        }
        matched.next
    }


    val titileWordMap = countList(recoreds.flatMap{case (artistName, title, numone) => title}
      .filter(word => !STOP_WORDS.contains(word)))

    val titleCount = titileWordMap.toList.sortBy{case (word, num) => -num}.map{case (word, num) => word}
    
    //a
    println(s"The most ${NUM_DISPLAY} frequent nontrivaial words  are ${titleCount.take(NUM_DISPLAY).mkString(",")}")

    //b
    val artistMap = countList(recoreds.map{case (artistName, title, numone) => artistName})
    val artistCnt = artistMap.toList.sortBy(tuple => -tuple._2).map{case (word, num) => word}
    println(s"The artists with the most ${NUM_DISPLAY} songs are ${artistCnt.take(NUM_DISPLAY).mkString(",")}")

    val numoneMap = countList(recoreds.filter{case (artistName, title, numone) => numone}
        .map{case (artistName, title, numone) => artistName})
    val numoneCnt = numoneMap.toList.sortBy{case (word, num) => -num}.map{case (word, num) => word}
    println(s"The artists with the most ${NUM_DISPLAY} numone songs are ${numoneCnt.take(NUM_DISPLAY).mkString(",")}")

    //c
    val frequences = titileWordMap.toList.sortBy{case (word, num) => -num}.take(FREQUENCE_THRESHOLD)
    val numoneTimes = recoreds.filter {case (artistName, title, numone)
      => numone
    }.length
    for ((word, _) <- frequences) {
      val all = recoreds.filter{case (artistName, title, numone) =>title.contains(word)}
      val desired = all.filter{case (artistName, title, numone) => numone}
      println(s"P(NUMONE|$word) = ${1.0 * desired.length / all.length}")
      println(s"P($word|NUMONE) = ${1.0 * desired.length / numoneTimes}")

    }

  }


}
