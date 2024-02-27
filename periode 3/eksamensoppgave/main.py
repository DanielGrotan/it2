import json
import os
from collections import defaultdict

from channel import Channel

ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def get_absolute_path(relative_path: str) -> str:
    return os.path.join(ABSOLUTE_DIR_PATH, relative_path)


def print_countries_with_most_channels(channels: list[Channel]) -> None:
    channel_counts = defaultdict(lambda: 0)

    for channel in channels:
        channel_counts[channel.country] += 1

    sorted_channel_counts = sorted(channel_counts.items(), key=lambda item: item[1], reverse=True)

    top_ten_countries = sorted_channel_counts[:10]

    print(f"The ten countries with the most amount of channels are: {", ".join(f"{country} ({channel_count})" for country, channel_count in top_ten_countries)}")

def print_countries_with_most_channels_detailed(channels: list[Channel]) -> None:
    country_statistics = defaultdict(lambda: {
        "channel_count": 0,
        "total_subscribers": 0,
        "total_views": 0
    })

    for channel in channels:
        statistics = country_statistics[channel.country]
        statistics["channel_count"] += 1
        statistics["total_subscribers"] += channel.subscribers
        statistics["total_views"] += channel.video_views
    
    sorted_channel_counts = sorted(country_statistics.items(), key=lambda item: item[1]["channel_count"], reverse=True)

    top_ten_countries = sorted_channel_counts[:10]

    print("Top 10 countries by channel count:")

    for country, statistics in top_ten_countries:
        print(country)
        print(f"Channel count: {statistics["channel_count"]}")
        print(f"Average subscribers: {statistics["total_subscribers"] / statistics["channel_count"]*1e-6:.2f} M")
        print(f"Average views: {statistics["total_views"] / statistics["channel_count"]*1e-6:.2f} M")
        print()

def main() -> None:
    with open(
        get_absolute_path("data/Global YouTube Statistics.json"), encoding="utf-8"
    ) as f:
        data = json.load(f)

    channels = [Channel(**channel) for channel in data]

    channels_with_country = list(filter(lambda channel: channel.country != "nan", channels))

    print_countries_with_most_channels(channels_with_country)
    print()
    print_countries_with_most_channels_detailed(channels_with_country)


if __name__ == "__main__":
    main()
