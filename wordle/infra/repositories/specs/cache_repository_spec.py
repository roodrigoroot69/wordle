from mamba import describe, context, it
from expects import expect, be_a, equal
from wordle.infra.repositories.cache_repository import RedisCacheRepository
from unittest.mock import Mock


with describe("RedisCacheRepository"):

    with context("save_attempt"):
        with it("saves an attempt"):
            mock_redis_client = Mock()
            repository = RedisCacheRepository(redis_client=mock_redis_client)
            key = "rodrigo"
            value = 3

            repository.save_attempt(key, value)

            mock_redis_client.set.assert_called_once_with(key, value, 300)

    with context("get_attempt"):
        with it("gets an attempt"):
            mock_redis_client = Mock()
            repository = RedisCacheRepository(redis_client=mock_redis_client)
            key = "rodrigo"
            mock_redis_client.get.return_value = "5"

            result = repository.get_attempt(key)

            expect(result).to(be_a(str))
            mock_redis_client.get.assert_called_once_with(key)

        with context(
            "whehn user make first attempt and does not exists a key-value in redis"
        ):
            with it("should return 1"):
                mock_redis_client = Mock()
                repository = RedisCacheRepository(redis_client=mock_redis_client)
                key = "DOES_NOT_EXISTS"
                mock_redis_client.get.return_value = None

                result = repository.get_attempt(key)

                expect(result).to(be_a(int))
                expect(result).to(equal(1))
                mock_redis_client.get.assert_called_once_with(key)
