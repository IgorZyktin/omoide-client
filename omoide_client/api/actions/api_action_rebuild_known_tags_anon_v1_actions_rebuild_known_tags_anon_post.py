from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_action_rebuild_known_tags_anon_v1_actions_rebuild_known_tags_anon_post_response_api_action_rebuild_known_tags_anon_v1_actions_rebuild_known_tags_anon_post import (
    ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/actions/rebuild_known_tags_anon",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost
]:
    if response.status_code == 202:
        response_202 = ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost.from_dict(
            response.json()
        )

        return response_202
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost
]:
    """Api Action Rebuild Known Tags Anon

     Recalculate all known tags for anon user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost
]:
    """Api Action Rebuild Known Tags Anon

     Recalculate all known tags for anon user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost
]:
    """Api Action Rebuild Known Tags Anon

     Recalculate all known tags for anon user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost
]:
    """Api Action Rebuild Known Tags Anon

     Recalculate all known tags for anon user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPostResponseApiActionRebuildKnownTagsAnonV1ActionsRebuildKnownTagsAnonPost
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed