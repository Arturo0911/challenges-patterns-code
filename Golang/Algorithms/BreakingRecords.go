package main

import "golang.org/x/exp/errors/fmt"

// Complete the breakingRecords function below.
func breakingRecords(scores [10]int32) [2]int32 {

	bestScore := 0
	worstScore := 0

	maxScore := 0
	minScore := 0
	counter := 0

	var finalScore [2]int32

	for i := 0; i < len(scores); i++ {

		if counter >= 1 {

			if scores[i] > int32(maxScore) {
				maxScore = int(scores[i])
				bestScore++
			}

			if scores[i] < int32(minScore) {
				minScore = int(scores[i])
				worstScore++
			}

		} else {

			maxScore = int(scores[i])
			minScore = int(scores[i])

		}
		counter++

	}

	finalScore[0] = int32(bestScore)
	finalScore[1] = int32(worstScore)

	return finalScore

}

func main() {

	var finalValues [10]int32 = [10]int32{3, 4, 21, 36, 10, 28, 35, 5, 24, 42} // Partial assignment
	fmt.Println(breakingRecords(finalValues))

}
