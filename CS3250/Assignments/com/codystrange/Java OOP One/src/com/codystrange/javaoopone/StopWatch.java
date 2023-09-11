package com.codystrange.javaoopone;

import java.time.Instant;
import java.time.Duration;
public class StopWatch {
    private Instant startTime;
    private Instant endTime;

    // A no-arg constructor that initializes startTime with the current time.
    public StopWatch() {
        this.startTime = Instant.now();
    }

    // A constructor that initializes startTime to a specified time.
    public StopWatch(Instant startTime) {
        this.startTime = startTime;
    }

    // Resets the startTime to the current time.
    public void start() {
        this.startTime = Instant.now();
    }

    // Sets the endTime to the current time.
    public void stop() {
        this.endTime = Instant.now();
    }

    // Returns the elapsed time for the stopwatch in milliseconds.
    public long getElapsedTime() {
        Duration duration = Duration.between(this.startTime, this.endTime);
        return duration.toMillis();
    }

    public Instant getStartTime() {
        return this.startTime;
    }

    public Instant getEndTime() {
        return this.endTime;
    }
}
