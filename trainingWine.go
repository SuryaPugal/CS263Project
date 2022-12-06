package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
	"github.com/sajari/regression"
)

func main() {
	// we open the csv file from the disk
	start := time.Now()
	f, err := os.Open("training2.csv")
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

	// In this case we are going to try and model our house price (y)
	// by the grade feature.
	var r regression.Regression
	r.SetObserved("quality")
	r.SetVar(0, "fixed acidity")
	r.SetVar(1, "volatile acidity")
	r.SetVar(2, "citric acid")
	r.SetVar(3, "residual sugar")
	r.SetVar(4, "chlorides")
	r.SetVar(5, "free sulfur dioxide")
	r.SetVar(6, "total sulfur dioxide")
	r.SetVar(7, "density")
	r.SetVar(8, "pH")
	r.SetVar(9, "fixed acidity")
	r.SetVar(10, "sulphates")
	r.SetVar(11, "alcohol ")


	// Loop of records in the CSV, adding the training data to the regressionvalue.
	for i, record := range records {
		// Skip the header.
		if i == 0 {
			continue
		}

		// Parse the house price, "y".
		price, err := strconv.ParseFloat(records[i][11], 64)
		if err != nil {
			log.Fatal(err)
		}

		// Parse the grade value.
		grade, err := strconv.ParseFloat(record[0], 64)
		if err != nil {
			log.Fatal(err)
		}

		// Add these points to the regression value.
		r.Train(regression.DataPoint(price, []float64{grade}))
	}

	// Train/fit the regression model.
	r.Run()
	// Output the trained model parameters.
	log.Printf("main, execution time %s\n", time.Since(start))
	fmt.Printf("\nRegression Formula:\n%v\n\n", r.Formula)
}

