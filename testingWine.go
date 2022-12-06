package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"math"
	"time"
	"os"
	"strconv"
)

func main() {
	// we open the csv file from the disk
	start := time.Now()
	f, err := os.Open("testing2.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	// we create a new csv reader specifying
	// the number of columns it has
	salesData := csv.NewReader(f)
	salesData.FieldsPerRecord = 12

	// we read all the records
	records, err := salesData.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	// by slicing the records we skip the header
	records = records[1:]
	// Loop over the test data predicting y
	observed := make([]float64, len(records))
	predicted := make([]float64, len(records))
	var sumObserved float64
	for i, record := range records {
		// Parse the house price, "y".
		price, err := strconv.ParseFloat(records[i][11], 64)
		if err != nil {
			log.Fatal(err)
		}
		observed[i] = price
		sumObserved += price

		// Parse the grade value.
		factor1, err := strconv.ParseFloat(record[0], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor2, err := strconv.ParseFloat(record[1], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor3, err := strconv.ParseFloat(record[2], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor4, err := strconv.ParseFloat(record[3], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor5, err := strconv.ParseFloat(record[4], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor6, err := strconv.ParseFloat(record[5], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor7, err := strconv.ParseFloat(record[6], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor8, err := strconv.ParseFloat(record[7], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor9, err := strconv.ParseFloat(record[8], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor10, err := strconv.ParseFloat(record[9], 64)
		if err != nil {
			log.Fatal(err)
		}
		factor11, err := strconv.ParseFloat(record[10], 64)
		if err != nil {
			log.Fatal(err)
		}

		// Predict y with our trained model.
		predicted[i] = predict(grade)
	}

	mean := sumObserved / float64(len(observed))
	for i := 0; i < len(observed); i++ {
		if predicted[i] > 0.9 * observed[i] && predicted[i] < * 1.1 *  {
			answer = answer + 1
		}
	}
	accuracy := answer / len(records)
	log.Printf("main, execution time %s\n", time.Since(start))
	// Output the R-squared to standard out.
	fmt.Printf("accuracy = %0.2f\n\n", accuracy)
}
