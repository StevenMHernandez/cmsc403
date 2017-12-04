import java.io.*;
import java.util.*;

public class Question8 {
    public static final String FILE_NAME = "SoccerStats.txt";

    public static final Integer TEAM_NAME = 0;
    public static final Integer LEAGUE = 1;
    public static final Integer GOALS = 2;
    public static final Integer SHOTS_PER_GAME = 3;
    public static final Integer POSSESSION_PERCENTAGE = 4;
    public static final Integer PASS_SUCCESS_PERCENTAGE = 5;
    public static final Integer AERIALS_WON = 6;

    public static void main(String[] arg) throws Exception {
        ArrayList<String[]> stats = Question8.loadFile();

        System.out.println("1: Print the team names and Leagues");
        System.out.println(String.format("%-24s %s", "  Team name", "  League"));
        stats.forEach((String[] team) -> System.out.println(String.format("%-24s %s", team[TEAM_NAME], team[LEAGUE])));


        System.out.println("2: Print the name and league of the teams that have scored over 5 goals");
        System.out.println(String.format("%-24s %-20s %s", "  Team name", "  League", "Goals"));
        stats.stream().filter((String[] team) -> (Integer.parseInt(team[GOALS]) > 5))
                .forEach(team -> System.out.println(String.format("%-24s %-20s %5s", team[TEAM_NAME], team[LEAGUE], team[GOALS])));


        System.out.println("3: Average the possession percentage");
        Double sum = stats.stream().map(team -> Double.parseDouble(team[POSSESSION_PERCENTAGE]))
                .reduce(0.0, (a, b) -> a + b);
        Double total = stats.stream().map(team -> 1.0).reduce(0.0, (a, b) -> a + b);
        System.out.println(sum / total);


        System.out.println("4: Sort the teams by league");
        Collections.sort(stats, (a, b) -> a[LEAGUE].compareTo(b[LEAGUE]));

        System.out.println(String.format("%-24s %-20s", "  Team name", "  League"));
        stats.stream().forEach(team -> System.out.println(String.format("%-24s %s", team[TEAM_NAME], team[LEAGUE])));


        System.out.println("5: Sort the teams by pass success percentage");
        System.out.println(String.format("%-24s %-20s %s", "  Team name", "  League", "Pass success percentage"));
        Collections.sort(stats, (a, b) -> (Double.parseDouble(a[PASS_SUCCESS_PERCENTAGE]) < Double.parseDouble(b[PASS_SUCCESS_PERCENTAGE]) ? 1 : -1));

        stats.stream().forEach(team -> System.out.println(String.format("%-24s %-20s %s", team[TEAM_NAME], team[LEAGUE], team[PASS_SUCCESS_PERCENTAGE])));


        System.out.println("6: Sort the team by league and aerials won");
        System.out.println(String.format("%-24s %-20s %s", "  Team name", "  League", "Aerials"));
        Collections.sort(stats, (a, b) -> a[LEAGUE].compareTo(b[LEAGUE]) == 0 ? (Double.parseDouble(a[AERIALS_WON]) < Double.parseDouble(b[AERIALS_WON]) ? 1 : -1) : a[LEAGUE].compareTo(b[LEAGUE]));

        stats.stream().forEach(team -> System.out.println(String.format("%-24s %-20s %5s", team[TEAM_NAME], team[LEAGUE], team[AERIALS_WON])));


        System.out.println("7: Reset each team’s goals to 0.");
        System.out.println(String.format("%-24s %-20s %s", "  Team name", "  League", "Goals"));
        stats.stream().map(team -> (team[GOALS] = "0") == "0" ? team : team)
                .forEach(team -> System.out.println(String.format("%-24s %-20s %5s", team[TEAM_NAME], team[LEAGUE], team[GOALS])));
    }

    public static ArrayList<String[]> loadFile() throws FileNotFoundException, IOException {
        FileInputStream fis = new FileInputStream(FILE_NAME);
        BufferedReader reader = new BufferedReader(new InputStreamReader(fis));

        ArrayList<String[]> values = new ArrayList<>();

        String line = reader.readLine();
        while (line != null) {
            String[] row = line.split("\t", -1);

            values.add(row);

            line = reader.readLine();
        }

        return values;
    }
}