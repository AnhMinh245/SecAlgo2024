package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
    "strconv"
)

func sieveOfEratosthenes(limit int) []bool {
    primes := make([]bool, limit+1)
    for i := 2; i <= limit; i++ {
        primes[i] = true
    }
    for p := 2; p*p <= limit; p++ {
        if primes[p] {
            for i := p * p; i <= limit; i += p {
                primes[i] = false
            }
        }
    }
    return primes
}

func generateQPrimes(primes []bool, limit int) []int {
    qPrimes := make(map[int]bool)
    for p := 2; p <= limit; p++ {
        if primes[p] {
            pCubed := p * p * p
            if pCubed <= limit {
                qPrimes[pCubed] = true
            }
            for q := p + 1; q <= limit; q++ {
                if primes[q] {
                    product := p * q
                    if product <= limit {
                        qPrimes[product] = true
                    }
                }
            }
        }
    }
    qPrimeList := make([]int, 0, len(qPrimes))
    for k := range qPrimes {
        qPrimeList = append(qPrimeList, k)
    }
    sort.Ints(qPrimeList)
    return qPrimeList
}

func main() {
    reader := bufio.NewReader(os.Stdin)
    input, _ := reader.ReadString('\n')
    T, _ := strconv.Atoi(input)

    cases := make([]int, T)
    maxN := 0
    for i := 0; i < T; i++ {
        input, _ := reader.ReadString('\n')
        cases[i], _ = strconv.Atoi(input)
        if cases[i] > maxN {
            maxN = cases[i]
        }
    }

    primes := sieveOfEratosthenes(maxN)
    qPrimes := generateQPrimes(primes, maxN)

    for _, n := range cases {
        count := 0
        for _, qPrime := range qPrimes {
            if qPrime <= n {
                count++
            } else {
                break
            }
        }
        fmt.Println(count)
    }
}
