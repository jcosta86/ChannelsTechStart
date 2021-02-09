import pytest

from dao.base_dao import BaseDao
from dao.channels_dao import ChannelsDao
from models.channels_model import Channels


class TestDaoChannels:
    @pytest.fixture
    def dao_instance(self):
        dao = ChannelsDao()
        return dao

    @pytest.fixture
    def channel_instance(self):
        channel = Channels('Name', 'description', 'contact@contato.com', 'www.teste.com', 0.2)
        return channel

    def test_instance(self, dao_instance):
        assert isinstance(dao_instance, BaseDao)

    def test_save(self, dao_instance, channel_instance):
        channel_saved = dao_instance.save(channel_instance)
        channel_from_data_base = dao_instance.read_by_id(channel_saved.id_)

        assert (channel_instance.name == channel_from_data_base.name)

        dao_instance.delete(channel_from_data_base)

    def test_read_all_database(self, dao_instance):
        result = dao_instance.read_all()

        assert isinstance(result, list)

    def test_read_by_id(self, dao_instance):
        result = dao_instance.read_all()
        id_ = result[0].id_
        channel_from_database = dao_instance.read_by_id(id_)

        assert isinstance(channel_from_database, Channels)

    def test_update(self, dao_instance, channel_instance):
        new_name = 'name_update_test'
        created = dao_instance.save(channel_instance)
        created.name = new_name
        channel_after_update = dao_instance.update(created)

        assert channel_after_update.name == new_name
        assert channel_after_update.id_ is not None
        assert isinstance(channel_after_update, Channels)

        dao_instance.delete(channel_after_update)

    def test_delete(self, dao_instance, channel_instance):
        created = dao_instance.save(channel_instance)
        id_ = created.id_
        dao_instance.delete(created)
        object_after_delete = dao_instance.read_by_id(id_)

        assert object_after_delete is None
