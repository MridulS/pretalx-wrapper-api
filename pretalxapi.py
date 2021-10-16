import requests
from requests.models import Response


class PreTalx:
    def __init__(self, domain: str, token: str = None) -> None:
        self.token = token
        self.domain = domain
        if token is None:
            self.headers = None
        else:
            self.headers = {"Authorization": f"Token {token}"}

    # Wrap the API with requests.get - https://docs.pretalx.org/api/index.html
    def get_events(self) -> Response:
        return requests.get(f"{self.domain}/api/events/", headers=self.headers)

    def get_event(self, event: str) -> Response:
        return requests.get(f"{self.domain}/api/events/{event}/", headers=self.headers)

    def get_submissions(self, event: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/submissions", headers=self.headers
        )

    def get_submission(self, event: str, code: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/submissions/{code}", headers=self.headers
        )

    def get_talks(self, event: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/talks", headers=self.headers
        )

    def get_talk(self, event: str, code: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/talks/{code}", headers=self.headers
        )

    def get_speakers(self, event: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/speakers", headers=self.headers
        )

    def get_speaker(self, event: str, code: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/speakers/{code}", headers=self.headers
        )

    def get_reviews(self, event: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/reviews", headers=self.headers
        )

    def get_review(self, event: str, code: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/reviews/{code}", headers=self.headers
        )

    def get_rooms(self, event: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/rooms", headers=self.headers
        )

    def get_room(self, event: str, code: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/rooms/{code}", headers=self.headers
        )

    def get_questions(self, event: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/questions", headers=self.headers
        )

    def get_question(self, event: str, code: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/questions/{code}", headers=self.headers
        )

    def get_answers(self, event: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/answers", headers=self.headers
        )

    def get_answer(self, event: str, code: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/answers/{code}", headers=self.headers
        )

    def get_tags(self, event: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/tags", headers=self.headers
        )

    def get_tag(self, event: str, code: str) -> Response:
        return requests.get(
            f"{self.domain}/api/events/{event}/tags/{code}", headers=self.headers
        )

    def validate_token(self) -> Response:
        return requests.get(f"{self.domain}/api/me", headers=self.headers)
