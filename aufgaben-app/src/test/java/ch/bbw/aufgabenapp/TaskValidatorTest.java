package ch.bbw.aufgabenapp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import java.time.LocalDate;
import java.util.stream.Stream;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class TaskValidatorTest {
    private final TaskValidator validator = new TaskValidator();
    private static final LocalDate TODAY = LocalDate.of(2026, 10, 20);

    static Stream<Arguments> titles() {
        return Stream.of(
            Arguments.of("TF-01", "", false),
            Arguments.of("TF-02", "a", true),
            Arguments.of("TF-03", "a".repeat(50), true),
            Arguments.of("TF-04", "a".repeat(100), true),
            Arguments.of("TF-05", "a".repeat(101), false),
            Arguments.of("TF-06", null, false),
            Arguments.of("TF-07", "   ", false),
            Arguments.of("TF-17", "\t\n", false)
        );
    }

    @ParameterizedTest(name = "{0}: Titel gültig = {2}")
    @MethodSource("titles")
    void title(String id, String value, boolean expected) {
        assertEquals(expected, validator.isTitleValid(value));
    }

    static Stream<Arguments> priorities() {
        return Stream.of(
            Arguments.of("TF-08", 0, false),
            Arguments.of("TF-09", 1, true),
            Arguments.of("TF-10", 3, true),
            Arguments.of("TF-11", 5, true),
            Arguments.of("TF-12", 6, false)
        );
    }

    @ParameterizedTest(name = "{0}: Priorität {1} gültig = {2}")
    @MethodSource("priorities")
    void priority(String id, int value, boolean expected) {
        assertEquals(expected, validator.isPriorityValid(value));
    }

    static Stream<Arguments> dates() {
        return Stream.of(
            Arguments.of("TF-13", TODAY.minusDays(1), false),
            Arguments.of("TF-14", TODAY, true),
            Arguments.of("TF-15", TODAY.plusDays(1), true),
            Arguments.of("TF-16", null, false)
        );
    }

    @ParameterizedTest(name = "{0}: Fälligkeit {1} gültig = {2}")
    @MethodSource("dates")
    void dueDate(String id, LocalDate value, boolean expected) {
        assertEquals(expected, validator.isDueDateValid(value, TODAY));
    }
}
