package ch.bbw.aufgabenapp;

import java.time.Clock;
import java.time.LocalDate;
import java.util.Objects;

public class TaskValidator {
    public static final int MAX_TITLE_LENGTH = 100;
    public static final int MIN_PRIORITY = 1;
    public static final int MAX_PRIORITY = 5;
    private final Clock clock;

    public TaskValidator() {
        this(Clock.systemDefaultZone());
    }

    public TaskValidator(Clock clock) {
        this.clock = Objects.requireNonNull(clock, "clock");
    }

    public boolean isTitleValid(String title) {
        if (title == null || title.isBlank()) {
            return false;
        }
        return title.codePointCount(0, title.length()) <= MAX_TITLE_LENGTH;
    }

    public boolean isPriorityValid(int priority) {
        return priority >= MIN_PRIORITY && priority <= MAX_PRIORITY;
    }

    public boolean isDueDateValid(LocalDate dueDate, LocalDate today) {
        Objects.requireNonNull(today, "today");
        return dueDate != null && !dueDate.isBefore(today);
    }

    public boolean isDueDateValid(LocalDate dueDate) {
        return isDueDateValid(dueDate, LocalDate.now(clock));
    }

    public boolean isValid(String title, int priority, LocalDate dueDate, LocalDate today) {
        return isTitleValid(title) && isPriorityValid(priority) && isDueDateValid(dueDate, today);
    }

    public boolean isValid(String title, int priority, LocalDate dueDate) {
        return isValid(title, priority, dueDate, LocalDate.now(clock));
    }
}
