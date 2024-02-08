from unittest.mock import Mock, call

from mamba import after, before, describe, context, it
from expects import expect, equal

from wordle.infra.repositories.cache_repository import RedisCacheRepository


with describe(RedisCacheRepository) as self:

    with before.all:
        self.ANY_KEY = 'rodrigo'
        self.ANY_VALUE = 'ANY_VALUE'
        self.redis_client_mock = Mock()
        self.redis_client_mock.get.return_value = 1
        self.redis_cache_repository = RedisCacheRepository(
            redis_client=self.redis_client_mock,
        )

    with context('get value from cache(redis)'):
        with it('if not exists a record return 1(first attempt)'):
            value = self.redis_cache_repository.get_attempt(key=self.ANY_KEY)

            expect(value).to(equal(1))

    with context('set value in cache'):
        with it('set expiration time'):
            self.redis_cache_repository.save_attempt(self.ANY_KEY, self.ANY_VALUE)

            expect(self.redis_client_mock.set.call_args).to(
                equal(
                    call('rodrigo','ANY_VALUE',300)
                ))
