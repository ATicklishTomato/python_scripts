import FlightRadar24
import config


def get_flights_to_print():
    fr_api = FlightRadar24.FlightRadar24API()

    bounds = fr_api.get_bounds_by_point(config.FLIGHT_COORDS["longitude"],
                                        config.FLIGHT_COORDS["latitude"],
                                        config.COORD_RADIUS)

    flights = fr_api.get_flights(bounds=bounds)

    printable_texts = []
    for flight in flights:
        flight_details = fr_api.get_flight_details(flight)
        flight.set_flight_details(flight_details)

        # If the altitude is higher than 10 000 feet, we don't want to print it.
        if flight.altitude > 10000:
            continue

        flight_text = "✈︎"
        flight_text += " Flight " + flight.number
        flight_text += ", Operator " + flight.airline_name
        flight_text += ", Aircraft " + flight.aircraft_model
        flight_text += ", From " + flight.origin_airport_name
        flight_text += ", Flying to " + flight.destination_airport_name
        flight_text += "."

        printable_texts.append(flight_text)

    return printable_texts


if __name__ == "__main__":
    strings = get_flights_to_print()
    for text in strings:
        print(text)
