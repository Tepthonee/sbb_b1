# Copyright (C) 2021 JepThon TEAM
# FILES WRITTEN BY  @lMl10l
import html

from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest

from sbb_b.Config import Config
from sbb_b.plugins import (
    ALIVE_NAME,
    BOTLOG,
    BOTLOG_CHATID,
    edit_delete,
    get_user_from_event,
    sbb_b,
)
from sbb_b.sql_helper.globals import gvarstatus
plugin_category = "utils"
DEFAULTUSER = gvarstatus("FIRST_NAME") or ALIVE_NAME
DEFAULTUSERBIO = Config.DEFAULT_BIO or "﴿ لا تَحزَن إِنَّ اللَّهَ مَعَنا ﴾"


@sbb_b.ar_cmd(pattern="انتحال(?:\s|$)([\s\S]*)")
async def _(event):
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user.id == 1050898456:
        return await edit_delete(event, "**لا تحاول تنتحل المطورين ادبسز!**")
    if replied_user.id == 1355571767:
        return await edit_delete(event, "**لا تحاول تنتحل المطورين ادبسز!**")
    if replied_user.id == 1099460779:
        return await edit_delete(event, "**لا تحاول تنتحل المطورين ادبسز!**")
    if replied_user is None:
         return
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = replied_user.about
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        pfile = await event.client.upload_file(profile_pic)
    except Exception as e:
        return await edit_delete(event, f"**فشل في الانتحال بسبب:**\n__{e}__")
    await event.client(functions.photos.UploadProfilePhotoRequest(pfile))
    await edit_delete(event, "**⌁︙تـم نسـخ الـحساب بـنجاح ،✅**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الانتحال\nتم انتحال المستخدم: [{first_name}](tg://user?id={user_id })",
        )


@sbb_b.ar_cmd(
    pattern="اعادة$",
    command=("اعادة", plugin_category),
    info={
        "header": "To revert back to your original name , bio and profile pic",
        "note": "For proper Functioning of this command you need to set AUTONAME and DEFAULT_BIO with your profile name and bio respectively.",
        "usage": "{tr}revert",
    },
)
async def _(event):
    "To reset your original details"
    name = f"{DEFAULTUSER}"
    blank = ""
    bio = f"{DEFAULTUSERBIO}"
    await event.client(
        functions.photos.DeletePhotosRequest(
            await event.client.get_profile_photos("me", limit=1)
        )
    )
    await event.client(functions.account.UpdateProfileRequest(about=bio))
    await event.client(functions.account.UpdateProfileRequest(first_name=name))
    await event.client(functions.account.UpdateProfileRequest(last_name=blank))
    await edit_delete(event, "⌁︙تـم اعـادة الـحساب بـنجاح ،✅")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, f"⌁︙تـم اعادة الـحساب الى وضـعه الاصلـي ،✅")
        
jeps = ["cr_source", "gro_up_1"]
@sbb_b.ar_cmd(pattern="انتحال_الدردشه")
async def reda(event):
    if event.is_group or event.is_channel:
        chat_id = -1
        msg = event.message.message
        msg = msg.replace(".انتحال_الدردشه", "")
        msg = msg.replace(" ", "")
        if msg == "":
            return await edit_delete(event, "**قم بوضع يوزر الگروب او القناة بدون علامة @ للانتحال**")
        chat_id = msg
        try:
            result = await jepiq(GetFullChannelRequest(
                chat_id
            ))
        except ValueError:
            return await edit_delete(event, "**᯽︙ لا يوجد هكذا كروب او قناة تاكد من اليوزر او الايدي ويجب ان يكون/تكون عام/عامة وليس خاص/خاصة**")
        mych = await jepiq(GetFullChannelRequest(
                event.chat_id
            ))
        if msg in jeps:
            return await edit_delete(event, "**᯽︙ لا يمكنك انتحال قناة او كروب السورس !**")
        addgvar(f"{event.chat_id}name", mych.chats[0].title)
        addgvar(f"{event.chat_id}about", mych.full_chat.about)
        try:
            await jepiq(functions.channels.EditTitleRequest(
                channel=await jepiq.get_entity(event.chat_id),
                title=result.chats[0].title
            ))
        except ChatAdminRequiredError:
            delgvar (f"{event.chat_id}name")
            delgvar (f"{event.chat_id}about")
            return await edit_delete(event, "**᯽︙ يجب ان تكون لديك صلاحيات لتغيير الاسم والصورة والبايو لانتحال قناة او كروب**")
        except FloodWaitError:
            return await edit_delete(event, "**انتضر مدة لا تقل عن 5 دقائق للانتحال مجدداً FLOODWAITERROR خطأ من التيليجرام**")
        try:
            await jepiq(functions.messages.EditChatAboutRequest(
            peer=event.chat_id,
            about=result.full_chat.about
        ))
        except FloodWaitError:
            return await edit_delete(event, "**انتضر مدة لا تقل عن 5 دقائق للانتحال مجدداً FLOODWAITERROR خطأ من التيليجرام**")
        profile_pic = await jepiq.download_profile_photo(chat_id, Config.TEMP_DIR)
        pfile = await jepiq.upload_file(profile_pic)
        try:
            await jepiq(functions.channels.EditPhotoRequest(event.chat_id, pfile))
        except FloodWaitError:
            return await edit_delete(event, "**انتضر مدة لا تقل عن 5 دقائق للانتحال مجدداً FLOODWAITERROR خطأ من التيليجرام**")
        await edit_delete(event, "**᯽︙ تم الانتحال بنجاح ✓**")
        base64m = 'QGplcHRob24='
        message = base64.b64decode(base64m)
        messageo = message.decode()
        if len(messageo) != 8:
            return await edit_delete(event, "لا تغير الرسالة @cr_source")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الانتحال\nتم إنتحال الدردشه @{msg}\n©{messageo}",
            )
    else:
        await edit_delete(event, "**᯽︙ يمكنك انتحال قناة او كروب في قناة او كروب فقط**")

#Reda
@sbb_b.ar_cmd(pattern="اعادة_الدردشه")
async def reda_back(event):
    if event.is_group or event.is_channel:
        if gvarstatus (f"{event.chat_id}name"):
            try:
                await jepiq(functions.channels.EditTitleRequest(
                    channel=await jepiq.get_entity(event.chat_id),
                    title=gvarstatus (f"{event.chat_id}name")
                ))
            except ChatAdminRequiredError:
                return await edit_delete(event, "**᯽︙ يجب ان تكون لديك صلاحيات لتغيير الاسم والصورة والبايو لإعادة القناة او الكروب**")
            except FloodWaitError:
                return await edit_delete(event, "**انتضر مدة لا تقل عن 5 دقائق لإعادة الدردشة مجدداً FLOODWAITERROR خطأ من التيليجرام**")
            await jepiq(functions.messages.EditChatAboutRequest(
            peer=event.chat_id,
            about=gvarstatus (f"{event.chat_id}about")
            ))
            async for photo in jepiq.iter_profile_photos(event.chat_id, limit=1) :
                    await jepiq(
                    functions.photos.DeletePhotosRequest(id=[types.InputPhoto( id=photo.id, access_hash=photo.access_hash, file_reference=photo.file_reference )])
                    )
            await edit_delete(event, "**᯽︙ تم إعادة الكروب/ القناة بنجاح**")
            delgvar (f"{event.chat_id}name")
            delgvar (f"{event.chat_id}about")
        else:
            await edit_delete(event, "**لم تقم بانتحال قناة او كروب للإعادة**")
    else:
        await edit_delete(event, "**᯽︙ يمكنك إعادة الدردشة المُنتحِله عبر كتابة الامر في الكروب او القناة المُنتحِله فقط**")
