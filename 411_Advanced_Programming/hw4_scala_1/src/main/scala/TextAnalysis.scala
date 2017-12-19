

import scala.io.Source

object TextAnalysis {
  def makeDict(raw: List[String]) = {
    raw.foldLeft(Map.empty[String, Int]) { (dict, word) => dict + (word -> (dict.getOrElse(word, 0) + 1)) }
  }

    

  def main(args: Array[String]): Unit = {

    val data = Source.fromFile("top40.sql").getLines().toList

    val tuples = data.map {
      case line =>
        //(1, 'ABBA', 'WATERLOO', 0);
        val pattern = "'([^']+)'[^']+'([^']+)',\\s+(\\d)".r
        val matched = pattern.findAllIn(line).matchData.map {
          case m =>
            val artistName = m.group(1)
            val rawTitle = m.group(2)
            val numone = m.group(3).filter { c => c == '0' | c == '1' }

            val title = rawTitle.replaceAll("[,\\.!]", " ").split("\\s+").map(_.toLowerCase)
            (artistName, title, numone)
        }
        matched.next
    }

    val trivialWords = Set("be", "of", "my", "your",  "on","you",
      "it", "me", "to",  "on",  "for", "is", "the",  "i", "a", "in")

    val nontrivals = tuples.flatMap{case (_, words, _) => words}
      .filter(word => !trivialWords.contains(word))

    val titileWordMap = makeDict(nontrivals)

    val wordCnt = titileWordMap.toList.sortBy(-_._2)
    
    //top K to be displayed
    val K = 5
    
    //a
    println(s"[(Top ${K})]The most frequent non trivaial words  are " + wordCnt.take(K).map(_._1))

    //b1
    val artistList = tuples.map(tuple => tuple._1)
    val artistMap = makeDict(artistList)
    val artistCnt = artistMap.toList.sortBy(tuple => -tuple._2)
    println(s"[(Top ${K})]The artists with the most top 40 songs are " + artistCnt.take(K).map(_._1))

    //b2
    val numone = tuples.filter(_._3 == "1").map(_._1)
    val numoneMap = makeDict(numone)
    val numoneCnt = numoneMap.toList.sortBy(-_._2)
    println(s"[(Top ${K})]The artists with the most numone songs are " + numoneCnt.take(K).map(_._1))

    val frequences = wordCnt.take(50)
    val numoneTimes = tuples.filter {
      _._3 == "1"
    }.length
    for ((word, _) <- frequences) {

      //c
      val all = tuples.filter(_._2.contains(word))
      val intersect = all.filter(_._3 == "1")
      println(s"P(numone|$word) = ${1.0 * intersect.length / all.length}")
      println(s"P($word|numone) = ${1.0 * intersect.length / numoneTimes}")

    }

  }


}