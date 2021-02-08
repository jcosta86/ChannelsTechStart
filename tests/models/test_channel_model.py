import sys

sys.path.append('.')
from models.channels_model import Channels

import pytest


class TestChannel:
    def test_channel_instance(self):
        channel = Channels('Name', 'description', 'contact@contato.com', 'www.teste.com', 0.2)
        assert isinstance(channel, Channels)

    @pytest.fixture
    def channel_instance(self):
        channel = Channels('Name', 'description', 'contact@contato.com', 'www.teste.com', 0.2)
        return channel

    @pytest.mark.parametrize('name', [10, 10.00, True])
    def test_channel_name_type(self, channel_instance, name):
        with pytest.raises(TypeError):
            channel_instance.name = name

    @pytest.mark.parametrize('name', ['', 'name' * 101])
    def test_channel_name_len_and_not_empty(self, channel_instance, name):
        with pytest.raises(ValueError):
            channel_instance.name = name

    @pytest.mark.parametrize('description', [10, 10.00, True])
    def test_channel_description_type(self, channel_instance, description):
        with pytest.raises(TypeError):
            channel_instance.description = description

    def test_channel_description_len(self, channel_instance):
        with pytest.raises(ValueError):
            channel_instance.description = 'description' * 256

    @pytest.mark.parametrize('contact', [10, 10.00, True])
    def test_channel_contact_type(self, channel_instance, contact):
        with pytest.raises(TypeError):
            channel_instance.contact = contact

    @pytest.mark.parametrize('contact', ['', 'contact' * 256])
    def test_channel_contact_len_and_not_empty(self, channel_instance, contact):
        with pytest.raises(ValueError):
            channel_instance.contact = contact

    @pytest.mark.parametrize('url', ['', 'url' * 256])
    def test_channel_url_len_and_not_empty(self, channel_instance, url):
        with pytest.raises(ValueError):
            channel_instance.url = url

    @pytest.mark.parametrize('url', [10, 10.00, True])
    def test_channel_url_type(self, channel_instance, url):
        with pytest.raises(TypeError):
            channel_instance.url = url

    @pytest.mark.parametrize('rate', ['a', True])
    def test_channel_rate_type(self, channel_instance, rate):
        with pytest.raises(TypeError):
            channel_instance.rate = rate

    def test_channel_rate_not_empty(self, channel_instance):
        with pytest.raises(TypeError):
            channel_instance.rate = ''
