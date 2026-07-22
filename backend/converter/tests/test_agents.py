from django.test import TestCase

from converter.agents.audio_agent import extract_audio


class AgentTests(TestCase):

    def test_audio_agent_exists(self):
        self.assertTrue(callable(extract_audio))