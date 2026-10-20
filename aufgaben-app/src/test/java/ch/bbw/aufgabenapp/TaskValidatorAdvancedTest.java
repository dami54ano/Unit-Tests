package ch.bbw.aufgabenapp;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.time.Clock;
import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneId;
import java.time.ZoneOffset;
import java.util.stream.Stream;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class TaskValidatorAdvancedTest {
    private static final LocalDate TODAY = LocalDate.of(2026, 10, 20);
    private static final Clock CLOCK = Clock.fixed(
        Instant.parse("2026-10-20T10:00:00Z"), ZoneId.of("Europe/Zurich"));
    private final TaskValidator validator = new TaskValidator(CLOCK);
    private static final String EMOJI = "\uD83D\uDE00";

    static Stream<Arguments> rules() {
        return Stream.of(
            Arguments.of("Z-01 / R1", "Aufgabe", 3, TODAY.plusDays(1), true),
            Arguments.of("Z-02 / R2", "", 3, TODAY.plusDays(1), false),
            Arguments.of("Z-03 / R3", "Aufgabe", 3, TODAY.minusDays(1), false),
            Arguments.of("Z-04 / R4", "Aufgabe", 0, TODAY.plusDays(1), false)
        );
    }

    @ParameterizedTest(name = "{0}: gesamte Aufgabe gültig = {4}")
    @MethodSource("rules")
    void decisionTable(String id, String title, int priority, LocalDate dueDate, boolean expected) {
        // Dasselbe fachliche Verhalten über beide öffentlichen Varianten.
        assertAll(
            () -> assertEquals(expected, validator.isValid(title, priority, dueDate, TODAY)),
            () -> assertEquals(expected, validator.isValid(title, priority, dueDate))
        );
    }

    static Stream<Arguments> clockDates() {
        return Stream.of(
            Arguments.of("Z-05", TODAY.minusDays(1), false),
            Arguments.of("Z-06", TODAY, true),
            Arguments.of("Z-07", TODAY.plusDays(1), true),
            Arguments.of("Z-08", null, false),
            Arguments.of("Z-18", LocalDate.MIN, false),
            Arguments.of("Z-19", LocalDate.MAX, true)
        );
    }

    @ParameterizedTest(name = "{0}: feste Clock, Fälligkeit {1} gültig = {2}")
    @MethodSource("clockDates")
    void fixedClock(String id, LocalDate dueDate, boolean expected) {
        assertEquals(expected, validator.isDueDateValid(dueDate));
    }

    @Test
    void Z09_zurichIsAlreadyNextDay() {
        Clock clock = Clock.fixed(Instant.parse("2026-10-19T22:30:00Z"), ZoneId.of("Europe/Zurich"));
        assertEquals(false, new TaskValidator(clock).isDueDateValid(LocalDate.of(2026, 10, 19)));
    }

    @Test
    void Z10_utcIsStillPreviousDay() {
        Clock clock = Clock.fixed(Instant.parse("2026-10-19T22:30:00Z"), ZoneOffset.UTC);
        assertEquals(true, new TaskValidator(clock).isDueDateValid(LocalDate.of(2026, 10, 19)));
    }

    static Stream<Arguments> unicodeTitles() {
        return Stream.of(
            Arguments.of("Z-11", EMOJI.repeat(100), 200, 100, true),
            Arguments.of("Z-12", EMOJI.repeat(101), 202, 101, false),
            Arguments.of("Z-13", EMOJI, 2, 1, true),
            Arguments.of("Z-14", "a".repeat(99) + EMOJI, 101, 100, true),
            Arguments.of("Z-15", "a".repeat(100) + EMOJI, 102, 101, false)
        );
    }

    @ParameterizedTest(name = "{0}: UTF-16-Länge {2}, Codepoints {3}, gültig = {4}")
    @MethodSource("unicodeTitles")
    void unicodeBoundary(String id, String title, int units, int points, boolean expected) {
        assertAll(
            () -> assertEquals(units, title.length()),
            () -> assertEquals(points, title.codePointCount(0, title.length())),
            () -> assertEquals(expected, validator.isTitleValid(title))
        );
    }

    static Stream<Arguments> extremePriorities() {
        return Stream.of(
            Arguments.of("Z-16", Integer.MIN_VALUE),
            Arguments.of("Z-17", Integer.MAX_VALUE)
        );
    }

    @ParameterizedTest(name = "{0}: extreme Priorität {1} abgelehnt")
    @MethodSource("extremePriorities")
    void extremePriority(String id, int priority) {
        assertEquals(false, validator.isPriorityValid(priority));
    }
}
