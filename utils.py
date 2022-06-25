import subprocess


def run_command(cmd: str):
	"""Runs a command and returns the output"""
	return str(subprocess.getoutput(cmd))


def get_artist():
	return run_command("playerctl metadata artist")


def get_title():
	return run_command("playerctl metadata title")


def is_playing():
	if run_command("playerctl status") == "Playing":
		return True
	return False


def is_song_title_already_formatted(title: str):
	split_title = title.split()
	try:
		if split_title.index("-") != 0 and split_title.index("-") != -1:
			return True
	except ValueError as exception:
		return False
