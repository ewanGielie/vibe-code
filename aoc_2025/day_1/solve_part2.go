package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	filename := "input.txt"
	if len(os.Args) > 1 {
		filename = os.Args[1]
	}

	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Printf("Error: %s not found.\n", filename)
		return
	}

	// Parse input: split by whitespace
	rotations := strings.Fields(string(content))

	currentPos := 50
	zeroCount := 0

	for _, rot := range rotations {
		if rot == "" {
			continue
		}

		direction := rot[0]
		amountStr := rot[1:]
		amount, err := strconv.Atoi(amountStr)
		if err != nil {
			fmt.Printf("Skipping invalid rotation: %s\n", rot)
			continue
		}

		distToZero := 0
		if direction == 'L' {
			// Moving towards 0: 50 -> 49 ... -> 0
			if currentPos != 0 {
				distToZero = currentPos
			} else {
				distToZero = 100
			}

			// Update position (Go's % operator can return negative for negative operands, but here operands are positive before %)
			// Actually, (currentPos - amount) can be negative.
			// (a % n + n) % n handles negative a correctly.
			currentPos = (currentPos - amount) % 100
			if currentPos < 0 {
				currentPos += 100
			}

		} else if direction == 'R' {
			// Moving towards 100 (which is 0): 50 -> 51 ... -> 99 -> 0
			if currentPos != 0 {
				distToZero = 100 - currentPos
			} else {
				distToZero = 100
			}

			// Update position
			currentPos = (currentPos + amount) % 100
		} else {
			fmt.Printf("Unknown direction in rotation: %s\n", rot)
			continue
		}

		if amount >= distToZero {
			// We hit 0 at least once
			hits := 1 + (amount-distToZero)/100
			zeroCount += hits
		}
	}

	fmt.Printf("Password: %d\n", zeroCount)
}
