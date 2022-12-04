package main

import (
    "encoding/csv"
    "time"    
    "log"
    "os"
    "fmt"
    "github.com/gocolly/colly"
)

func main() {
    start := time.Now()
    fName := "data.csv"
    file, err := os.Create(fName)
    if err != nil {
        log.Fatalf("Could not create file, err: %q", err)
        return
    }
    defer file.Close()

    writer := csv.NewWriter(file)
    defer writer.Flush()

    fmt.Println("Scrapping Start")
    c := colly.NewCollector()
    c.OnHTML("table", func(e *colly.HTMLElement) {
        fmt.Println("Scrapping In loop")
        e.ForEach("tr", func(_ int, el *colly.HTMLElement) {
            writer.Write([]string{
                el.ChildText("td:nth-child(1)"),
                el.ChildText("td:nth-child(2)"),
                el.ChildText("td:nth-child(3)"),
                el.ChildText("td:nth-child(4)"),
                el.ChildText("td:nth-child(5)"),
                el.ChildText("td:nth-child(6)"),
                el.ChildText("td:nth-child(7)"),
                el.ChildText("td:nth-child(8)"),
            })
        })
        fmt.Println("Scrapping Complete")
    })
    c.Visit("https://www.ndbc.noaa.gov/station_page.php?station=46054")
    log.Printf("main, execution time %s\n", time.Since(start))
}
